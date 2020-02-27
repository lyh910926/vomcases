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
      path: ../../src_py/sce_stats_best.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: 12
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_11:
    default: w
    inputBinding:
      position: 11
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_12:
    default: 3
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_13:
    default: o
    inputBinding:
      position: 13
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default:
      class: File
      path: ../../data/fPAR/fpar_howard_v5.txt
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default: d
    inputBinding:
      position: 15
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_16:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default: data/VOM_output/additional_analyses/sens_esoil/HS_0.20/sce_stats_best
    inputBinding:
      position: 17
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/sens_esoil/HS_0.20/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: o
    inputBinding:
      position: 3
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default: o
    inputBinding:
      position: 5
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: 5
    inputBinding:
      position: 7
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default: 9
    inputBinding:
      position: 8
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_9:
    default: w
    inputBinding:
      position: 9
      prefix: -s
      separate: false
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_17)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/additional_analyses/sens_esoil/HS_0.20/sce_stats_best
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/sce_stats_best.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/additional_analyses/sens_esoil/HS_0.20/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/fPAR/fpar_howard_v5.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
