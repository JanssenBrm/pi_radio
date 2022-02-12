# PI Radio 🍇

![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![](https://img.shields.io/github/last-commit/janssenbrm/pi_radio?style=for-the-badge)

With the goal to put my Raspberry Pi to use as a streaming stataion, I've created this general purpose project. Using
the `flask` library, the code in this project will start a small webserver that serves a main webpage. By using the
controls on this page, a user can select to play/pause an online audio stream and change the volumen. Because everything
is controlled through a webpage, that is hosted by the device running the code, any other device on the same network can
be used to control what is being played.

In my case, I have used this project to turn my Raspberry Pi into a device that is able to play my favorite online radio
streams. After hooking up my Raspberry Pi to a set of speakers in the garden, I can now listen to some music outdoors.
And the best thing of it all, I can easily control what is being played by using my smartphone!

![](https://github.com/JanssenBrm/pi_radio/blob/master/screenshots/pi_radio.png)

## Try it yourself!

Before you start exploring the project, make sure the following prerequisites are installed on your machine/device:

* `mpc` [](https://www.musicpd.org/clients/mpc/) - This library is required to control the playback of online streams
  and volume controls.
* Python

Using the `conf/stations.json`, you can configure a set of online streams to provide on the main webpage. The only thing
left for you to do is to start the `app.py` script and listen to your tunes 🎵🤘🤘
