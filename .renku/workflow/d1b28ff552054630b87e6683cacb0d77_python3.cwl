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
    default: VOM
    inputBinding:
      position: 10
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 11
      prefix: --obs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default: 1000
    inputBinding:
      position: 12
      prefix: --mf
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_13:
    default: 'True'
    inputBinding:
      position: 13
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: data/img/additonal_plots/hs_evap.png
    inputBinding:
      position: 14
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: evaptot
    inputBinding:
      position: 3
      prefix: -v
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: s
    inputBinding:
      position: 4
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: 2010
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_6:
    default: e
    inputBinding:
      position: 6
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: 2015
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/dailyweather.prn
    inputBinding:
      position: 8
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: Etot [mm/d]
    inputBinding:
      position: 9
      prefix: --ylabel
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_14)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img/additonal_plots
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_et_ass.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/VOM_input/HowardSprings/dailyweather.prn
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
successCodes: []
temporaryFailCodes: []
