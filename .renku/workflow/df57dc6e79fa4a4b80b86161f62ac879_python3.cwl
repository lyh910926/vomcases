arguments:
- position: 17
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
- position: 20
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
      path: ../../src_py/plot_et_ass_gw_sm.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: 30
    inputBinding:
      position: 10
      prefix: --i_cz
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_11:
    default: 5
    inputBinding:
      position: 11
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default: 16
    inputBinding:
      position: 12
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_13:
    default: 25
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_litch.txt
    inputBinding:
      position: 14
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 15
      prefix: --pars
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default: 'True'
    inputBinding:
      position: 16
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: '.12'
    inputBinding:
      position: 18
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_19:
    default: 24
    inputBinding:
      position: 19
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default: 5
    inputBinding:
      position: 21
      prefix: '-3'
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_22:
    default: 0
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_23:
    default: 'True'
    inputBinding:
      position: 23
      prefix: --title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_24:
    default:
      class: File
      path: ../../data/VOM_soils/Litchfield/soilprofile.par
    inputBinding:
      position: 24
      prefix: --soildata
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/DINGO/Ea_litch.txt
    inputBinding:
      position: 25
      prefix: --obs_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_litch.txt
    inputBinding:
      position: 26
      prefix: --obs_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/fPAR/fpar_litchfield_v5.txt
    inputBinding:
      position: 27
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 28
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default: data/img/additonal_plots/lf_gw_sm_et_ass.png
    inputBinding:
      position: 29
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default: 'True'
    inputBinding:
      position: 3
      prefix: --depth
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
    default: 2015
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
    default: 2017
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default: VOM
    inputBinding:
      position: 8
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: red
    inputBinding:
      position: 9
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_29)
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
    entryname: src_py/plot_et_ass_gw_sm.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/DINGO_SWS/SWSCon_litch.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: work/Litchfield/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/VOM_soils/Litchfield/soilprofile.par
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/DINGO/Ea_litch.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/DINGO/GPPdaily_litch.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/fPAR/fpar_litchfield_v5.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
