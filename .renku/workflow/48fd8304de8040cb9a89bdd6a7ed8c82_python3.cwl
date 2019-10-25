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
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.8/sce_best/results_daily.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.0/sce_best/results_daily.txt
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.2/sce_best/results_daily.txt
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.4/sce_best/results_daily.txt
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.6/sce_best/results_daily.txt
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff2.8/sce_best/results_daily.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff3.0/sce_best/results_daily.txt
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default: evaptot
    inputBinding:
      position: 17
      prefix: -v
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: s
    inputBinding:
      position: 18
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_19:
    default: 2011
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.2/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default: e
    inputBinding:
      position: 20
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_21:
    default: 2015
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_22:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/dailyweather.prn
    inputBinding:
      position: 22
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 23
      prefix: --obs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default: 1000
    inputBinding:
      position: 24
      prefix: --mf
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_25:
    default: Etot [mm/d]
    inputBinding:
      position: 25
      prefix: --ylabel
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_26:
    default: '3.0'
    inputBinding:
      position: 26
      prefix: --cbar_max
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_27:
    default: 'True'
    inputBinding:
      position: 27
      prefix: --plot_cbar
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_28:
    default: cpcff ($\mu mol m^3 s^-1)$
    inputBinding:
      position: 28
      prefix: --cblabel
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: VOM
    inputBinding:
      position: 29
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.4/sce_best/results_daily.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: VOM2
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default: img/HS_evap_cpcff.png
    inputBinding:
      position: 31
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_best/results_daily.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce_best/results_daily.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce_best/results_daily.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.4/sce_best/results_daily.txt
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.6/sce_best/results_daily.txt
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_31)
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
  - entry: $(inputs.input_1)
    entryname: src_py/plot_et_ass.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.2/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.4/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.6/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.4/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.6/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.8/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.2/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.4/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.6/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.8/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff3.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/VOM_input/HowardSprings/dailyweather.prn
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
successCodes: []
temporaryFailCodes: []
