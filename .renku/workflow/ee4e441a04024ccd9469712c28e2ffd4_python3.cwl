arguments:
- position: 21
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
- position: 24
  separate: true
  shellQuote: true
  valueFrom: --ylim
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_gw_sm_ws.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/boreholes/RN030984.csv
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_howard.txt
    inputBinding:
      position: 11
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default: VOM
    inputBinding:
      position: 12
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: red
    inputBinding:
      position: 13
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: 30
    inputBinding:
      position: 14
      prefix: --i_cz
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default: 5
    inputBinding:
      position: 15
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_16:
    default: 16
    inputBinding:
      position: 16
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_17:
    default: 25
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_18:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_howard.txt
    inputBinding:
      position: 18
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 19
      prefix: --pars
      separate: true
      shellQuote: true
    streamable: false
    type: File
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
  input_20:
    default: 'True'
    inputBinding:
      position: 20
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default: '.12'
    inputBinding:
      position: 22
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_23:
    default: 24
    inputBinding:
      position: 23
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_25:
    default: 5
    inputBinding:
      position: 25
      prefix: '-3'
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_26:
    default: 0
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_27:
    default: 'True'
    inputBinding:
      position: 27
      prefix: --title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_28:
    default:
      class: File
      path: ../../data/VOM_soils/HowardSprings/soilprofile.par
    inputBinding:
      position: 28
      prefix: --soildata
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    inputBinding:
      position: 29
      prefix: --i2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: 'True'
    inputBinding:
      position: 3
      prefix: --depth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default: 15
    inputBinding:
      position: 30
      prefix: --i_cz2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_31:
    default: 10
    inputBinding:
      position: 31
      prefix: --i_zr2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_32:
    default: '0.065'
    inputBinding:
      position: 32
      prefix: --i_thetar2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_33:
    default: '0.41'
    inputBinding:
      position: 33
      prefix: --i_thetas2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_34:
    default: data/img/additonal_plots/hs_gw_sm_ws.png
    inputBinding:
      position: 34
      prefix: --outputfile
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
    default: 2001
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
    default: 2005
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default:
      class: File
      path: ../../data/boreholes/RN030982.csv
    inputBinding:
      position: 8
      prefix: --obs_gw
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/boreholes/RN030983.csv
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_34)
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
    entryname: src_py/plot_gw_sm_ws.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/boreholes/RN030982.csv
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/boreholes/RN030983.csv
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/boreholes/RN030984.csv
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO_SWS/SWSCon_howard.txt
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/DINGO_SWS/SWSCon_howard.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/VOM_soils/HowardSprings/soilprofile.par
    writable: false
  - entry: $(inputs.input_29)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    writable: false
successCodes: []
temporaryFailCodes: []
