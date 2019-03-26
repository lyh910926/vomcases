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
      path: ../../src_py/plot_et_ass.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: e
    inputBinding:
      position: 10
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default: 2009
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default:
      class: File
      path: ../../data/VOM_input/AdelaideRiver/dailyweather.prn
    inputBinding:
      position: 12
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/nofreedrainage_cpcff1.0/bestruns/resultsdaily_best.txt
    inputBinding:
      position: 13
      prefix: -b
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default: evaporation
    inputBinding:
      position: 14
      prefix: -v
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default: img/evap_adelaide1.0nofree.png
    inputBinding:
      position: 15
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default: 1
    inputBinding:
      position: 2
      prefix: -m
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/nofreedrainage_cpcff1.0/bestruns/resultsdaily_max.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: 2
    inputBinding:
      position: 4
      prefix: -m
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_5:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/nofreedrainage_cpcff1.0/bestruns/resultsdaily_min.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: b
    inputBinding:
      position: 6
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default:
      class: File
      path: ../../data/DINGO/Ea_adelaide.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default: s
    inputBinding:
      position: 8
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: 2007
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: int
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_15)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: img
    writable: true
successCodes: []
temporaryFailCodes: []
