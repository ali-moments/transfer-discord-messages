# transfer-discord-messages

A short script to move all the links to the song files from a Discord group to the channel of a Discord server.

## Music Transfer Script

Actually, I wrote this script when I wanted to transfer the links of songs that were in a Discord group to a Discord channel. That's why the code is still on copying the links that lead to the music, and this code is currently not transmitting all the messages.
It will identify each message that contains a link to a music and send it to the desired channel.

Supported platforms:

- Youtube
- Spotify
- Soundcloud
- Apple Music
- Tidal
- Amazon Music
- Pandora
- Deezer

## Usage

1. Clone this repository:
   `git clone https://github.com/ali-moments/transfer-discord-messages`
2. Nvaigate to directory:
   `cd transfer-discord-messages`
3. Install dependencies using pip:
   `pip3 install -r requirements.txt`
4. Edit `TOKEN`, `SOURCE_CHANNEL_ID` and `DESTINATION_CHANNEL_ID` in [main.py](main.py) file.
5. Run the script with the following command:
   `python3 main.py`

> :warning: **Warning:** Bot should have proper permission to see and send messages.
> :memo: **Note:** you have to get a discord bot token from [discord developer portal](https://discord.com/developers/applications)

## Dependencies

This script requires the following dependencies:

- [Discord.py](https://pypi.org/project/discord.py/)

## License

This project is licensed under the Apache license. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please [open an issue](https://github.com/ali-moments/transfer-discord-messages/issues). If you would like to contribute code, please [fork the repository](https://github.com/ali-moments/transfer-discord-messages/forks) and submit a pull request.

## Credits

@ali-moments
