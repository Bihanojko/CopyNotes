import sys
import xml.etree.ElementTree as ET
import re
import io



def open_file(filepath, mode):
    try:
        return io.open(filepath, mode=mode, encoding="utf-8")
    except IOError:
        print('Error: Unable to open file: ' + filepath)
        raw_input('Press enter to exit...')
        sys.exit(5)



def get_logins():

    try:
        logins_file = open_file('logins.txt', 'r')
    except IOError:
        print('Error: Unable to open file: ' + logins_file)
        raw_input('Press enter to exit...')
        sys.exit(5)

    content = logins_file.read()
    logins_file.close()

    user_login = re.search('user_login=.+', content)
    user_login = user_login.string[user_login.start():user_login.end()]
    user_login = user_login[user_login.find("=") + 1:].strip()

    copy_from_logins = []

    for m in re.finditer('copy_from_login=.+', content):
        login = m.string[m.start():m.end()]
        copy_from_logins.append(login[login.find("=") + 1:].strip())

    return user_login, copy_from_logins



def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i



def main():

    user_login, copy_from_logins = get_logins()

    user_filename = 'notes.' + user_login + '.xml'
    try:
        user_tree = ET.parse(user_filename)
    except IOError:
        print('\nError: No such file or directory: ' + user_filename)
        raw_input('Press enter to exit...')
        sys.exit(5)
    user_root = user_tree.getroot()

    print "Copying notes to:\t" + user_filename 

    for login in copy_from_logins:
        copy_from_filename = 'notes.' + login + '.xml'
        print "from:\t\t\t" + copy_from_filename
        try:
            tree_copy_from = ET.parse(copy_from_filename).getroot()
        except IOError:
            print('\nError: No such file or directory: ' + copy_from_filename)
            raw_input('Press enter to exit...')
            sys.exit(5)

        for note in tree_copy_from.findall('note'):
            if note.text != None:
                player_found = False
                player = note.get('player')

                for comment in user_root.findall('note'):
                    if comment.get('player') == player:
                        player_found = True

                        if comment.text is None:
                            comment.text = "//////////////\n\n" + login + ": " + note.text.strip()
                  
                        else:
                            for src_note in note.text.split("//////////////"):
                                if re.search(r'\S+', src_note) != None:
                                    if src_note.split(' ', 1)[0][-1] != ':':
                                        src_note_login = login

                                        login_found = False
                                        whole_comment_content = ''
                                        for dst_note in comment.text.split("//////////////"):
                                            if re.search(r'\S+', dst_note) != None:
                                                if dst_note.split(' ', 1)[0][-1] == ':':
                                                    dst_note_login = dst_note.split(' ', 1)[0][:-1]
                                                    dst_note_login = dst_note_login.strip()
                                                    if dst_note_login == src_note_login:
                                                        login_found = True
                                                        comment.text = whole_comment_content + "//////////////\n\n" + src_note_login + ": " + src_note
                                                        dst_note = ''
                                            whole_comment_content += dst_note                                            

                                        if not login_found:
                                            comment.text += "\n\n//////////////\n\n" + src_note_login + ": " + src_note.strip()

                                    else:
                                        src_note_login = src_note.split(' ', 1)[0][:-1]
                                        src_note_login = src_note_login.strip()

                                        if src_note_login != user_login:
                                            login_found = False
                                            for dst_note in comment.text.split("//////////////"):
                                                if re.search(r'\S+', dst_note) != None:
                                                    if dst_note.split(' ', 1)[0][-1] == ':':
                                                        dst_note_login = dst_note.split(' ', 1)[0][:-1]
                                                        dst_note_login = dst_note_login.strip()
                                                        if dst_note_login == src_note_login:
                                                            login_found = True
                                                            break

                                            if not login_found:
                                                comment.text += "\n\n//////////////\n\n" + src_note.strip()
                        break

                if player_found is False:
                    add_note = ET.Element('note')
                    add_note.set("player", player)
                    add_note.set("label", "-1")
                    add_note.set("update", note.get('update'))
                    add_note.text = "//////////////\n\n" + login + ": " + note.text.strip()

                    pos = 0
                    for node in user_root.findall('note'):
                        if node.get('player') < player:
                            pos += 1
                        else:
                            break
                    user_root.insert(pos, add_note)

    indent(user_root)
    user_tree.write(user_filename, encoding="UTF-8", xml_declaration=True)

    raw_input('\nNotes copied successfully!\nPress enter to exit...')
    sys.exit(0)


if __name__ == "__main__":
    main()
