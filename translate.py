import json

def parse_songs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    songs = []
    current_song = None
    current_verse = None
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line[0].isdigit() and '-' in line:
            print('Song title:', line)
            if current_song:
                songs.append(current_song)
            song_number, song_title = line.split('-', 1)
            current_song = {
                'number': int(song_number.strip()),
                'title': song_title.strip(),
                'verses': [],
                'has_refrain': False,
                'refrain': ''
            }
        elif line.startswith('Fiv'):
            current_song['has_refrain'] = True
            current_song['refrain'] = line.split(':', 1)[1].strip()
        elif line.isdigit() and current_song:
            current_verse = {'number': int(line), 'lines': []}
            current_song['verses'].append(current_verse)
        elif current_song and current_verse:
            current_verse['lines'].append(line)

    if current_song:
        songs.append(current_song)

    return songs

def main():
    input_file = 'liste_chants.txt'
    output_file = 'liste_chants.json'

    songs = parse_songs(input_file)

    print(f'Found {len(songs)} songs')

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(songs, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
