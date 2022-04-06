import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.transforms.window as window
import re

input_file = '/app/words.txt'
output_path = '/app/cleaned.txt'

def run():
    options = PipelineOptions([
        "--runner=FlinkRunner",
        "--flink_version=1.13",
        "--flink_master=localhost:8081"
    ])

    with beam.Pipeline(options=options) as pipeline:
        (pipeline
            | 'Read Text file' >> beam.io.ReadFromText(input_file)
            | 'Split words'    >> beam.FlatMap(lambda words: words.split(' '))
            | 'Clean words'    >> beam.Map(lambda word: re.sub('[^A-Za-z]+','', word))
            | 'Write to file'  >> beam.io.WriteToText(output_path)
        )

if __name__ == "__main__":
    run()