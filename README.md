# TextSpam
## a small program to spam messages to scammers
please forgive my formatting I'm still figuring out how to use Markdown

## *Warnings*
- try not to click away from the program while its running: can mess up code or cause other weird effects
- test on a text document using a small number of repetitions first to get a feel for how it works
- some websites dont like how fast the program produces messages so you might have to adjust the replay speed
- if you're sending a lot of messages be prepared to let the script to run for a while
## How to use V2
### basic usage
- Send your first message as normal (using the enter key)
- hit the 'esc' key to replay your keystrokes a set number of times
### changing number of messages and replay speed
  to change the number of messages sent replace the number inside of the parenthesis after range.
  ```sh
  for i in range(10000):
  ```
  to change the speed at which your message is replayed change the speed factor(keystroke speed is dependent on this value as well as your typing speed)
  ```sh
  keyboard.play(recorded, speed_factor=100)
  ```
  ## How to use V1
  ### basic usage
  same as V2
  ### to change the number of messages and replay speed
  to change the number of messages sent change the number on this line.
  
  (alternaitivly you can change where the counter starts but it isnt recommeded as it is more confusing)
  ```sh
 while count <= 10000:
  ```
  to change the playback speed follow the same procedure as V2
  
  <!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* thanks to everyone on reddit for the help with formatting and code contact me through reddit if you want ot be directly metioned
* [https://github.com/othneildrew/Best-README-Template] (my help formatting my read me)

