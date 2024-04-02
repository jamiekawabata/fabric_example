# Example Plugin with Using Python Functions

This plugin mimics some of the functionality of Fabric.  Specifically getting the transcript of a YouTube video and "extracting wisdom" using LLM processing on the transcript.

This also demonstrates how dependencies on pip packages can be specified by a plugin and installed when the plugin is installed.  This allows extra Python functionality to be loaded when it is used, and the core server can remain relatively lightweight.