# equity_analyst


       +-----------------------------------------------+
       |                    Rationale                 |
       |   (Extend pain detection with multi-modal data) |
       +-----------------------------------------------+
                           |
                           v
                  +----------------+
                  |  Data Construction  |
                  +----------------+
                           |
                           v
          +---------------------------------+
          |  Data Annotation Process       |
          |  (AI-assisted, manually curated)|
          +---------------------------------+
                           |
                           v
                +-------------------------+
                | Video Data Processing    |
                | Workflow                  |
                +-------------------------+
                           |
    +----------------------+----------------------+
    |                      |                      |
    v                      v                      v
 +-----------+         +-----------+          +---------------------+
 | Face Detection|       | Video Segmentation|      | Mean & Standard Deviation |
 | and Cropping  |       | (5-second clips)    |      | (Normalization)         |
 +-----------+         +-----------+          +---------------------+
          |                     |                      |
          v                     v                      v
    +-----------------------------------------------+  
    | Video File Handling & Organization (Folder Structure)|
    +-----------------------------------------------+  
                           |
                           v
                 +----------------------+
                 | Transformation & Sampling|
                 +----------------------+
                           |
                           v
          +----------------------------------+
          | Data Augmentation (Training/Validation) |
          +----------------------------------+
                           |
                           v
             +-----------------------------+
             | Model Architecture: VideoMAEForVideoClassification |
             +-----------------------------+
                           |
         +-----------------+-----------------+
         |                 |                 |
         v                 v                 v
  +------------+     +------------+    +----------------+
  | Embeddings |     | Encoder    |    | Classifier     |
  +------------+     +------------+    +----------------+
         |
         v
   +----------------------+
   | Final Layer Normalization |
   +----------------------+
                           |
                           v
             +----------------------------+
             | Output (Pain Class Prediction)|
             | (NoPain, LowPain, MediumPain, HighPain)|
             +----------------------------+
