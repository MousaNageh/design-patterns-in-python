'''
Scenario: Online Video Player
Imagine you're designing an online video player system. The video player can have several states, 
such as Playing, Paused, Stopped, and Buffering. Each state has different behaviors associated with user actions or system events:


Playing: The video is currently playing. User actions could include pausing the video, stopping it, or the system might automatically switch to buffering if the internet speed slows down.
Paused: The video is paused. Users can resume playing the video or stop it.
Stopped: The video is stopped, and the user can choose to play it again from the beginning.
Buffering: The video is buffering due to slow internet speeds. Once enough data is buffered, the video automatically resumes playing from where it left off. Users can choose to pause or stop the video during buffering as well.
'''
from abc import ABC, abstractmethod
from typing import Optional

class Video:
    def __init__(self, name: str) -> None:
        self.name = name
        self.state: Optional[VideoState] = None
        self.position = 0  # For example, track video play position

    def change_state(self, state: 'VideoState'):
        self.state = state
        self.state.action(self)


class VideoState(ABC):
    @abstractmethod
    def action(self, video: Video):
        pass

class PlayVideo(VideoState):
    def action(self, video: Video):
        print('Playing the video:', video.name)
        # Implement logic for playing video

class PauseVideo(VideoState):
    def action(self, video: Video):
        print('Pausing the video:', video.name)
        # Implement logic for pausing video

class StopVideo(VideoState):
    def action(self, video: Video):
        print('Stopping the video:', video.name)
        video.position = 0  # Reset video position

class BufferVideo(VideoState):
    def action(self, video: Video):
        print('Buffering the video:', video.name)
        # Implement logic for buffering video


class VideoPlayer:
    def __init__(self, video: Video) -> None:
        self.video = video
        # Setting an initial state, e.g., stopped.
        self.video.change_state(StopVideo())

    def play(self):
        print("Request to play the video.")
        self.video.change_state(PlayVideo())

    def pause(self):
        print("Request to pause the video.")
        self.video.change_state(PauseVideo())

    def stop(self):
        print("Request to stop the video.")
        self.video.change_state(StopVideo())

    def buffer(self):
        print("Request to buffer the video.")
        self.video.change_state(BufferVideo())