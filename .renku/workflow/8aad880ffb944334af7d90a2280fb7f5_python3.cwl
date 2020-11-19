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
      path: ../../src_py/plot_roots.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 10
      prefix: --in4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 11
      prefix: --in5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default: '6.5'
    inputBinding:
      position: 12
      prefix: --spa_rtdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: 5
    inputBinding:
      position: 13
      prefix: --maespa_rtdepth
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: '4.5'
    inputBinding:
      position: 14
      prefix: --cable_rtdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default: '5.0'
    inputBinding:
      position: 15
      prefix: --bios2_rtdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_16:
    default: '2.0'
    inputBinding:
      position: 16
      prefix: --lpj_rtdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_17:
    default: '6.5'
    inputBinding:
      position: 17
      prefix: --spa_rgdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: '5.0'
    inputBinding:
      position: 18
      prefix: --maespa_rgdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_19:
    default: '4.5'
    inputBinding:
      position: 19
      prefix: --cable_rgdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default: Howard Springs
    inputBinding:
      position: 2
      prefix: --sites
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_20:
    default: '0.5'
    inputBinding:
      position: 20
      prefix: --bios2_rgdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_21:
    default: '2.0'
    inputBinding:
      position: 21
      prefix: --lpj_rgdepth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default: data/img/10_rootdepths.png
    inputBinding:
      position: 22
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default: Adelaide River
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: Daly River
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: Dry River
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: Sturt Plains
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 7
      prefix: --in1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 8
      prefix: --in2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 9
      prefix: --in3
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_22)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_roots.py
    writable: false
  - entry: $(inputs.input_7)
    entryname: work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: work/AdelaideRiver/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: work/DalyUncleared/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: work/DryRiver/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: work/SturtPlains/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
successCodes: []
temporaryFailCodes: []
