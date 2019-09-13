arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/write_pcseries.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: d
    inputBinding:
      position: 3
      prefix: -i
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default: 01-01-1980
    inputBinding:
      position: 5
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: 31-12-2017
    inputBinding:
      position: 6
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: work/additional_analyses/prescribed_cover/DalyUncleared/input/perc_cov.txt
    inputBinding:
      position: 7
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: 'True'
    inputBinding:
      position: 8
      prefix: --plot
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_7)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/additional_analyses/prescribed_cover/DalyUncleared/input
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/write_pcseries.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
