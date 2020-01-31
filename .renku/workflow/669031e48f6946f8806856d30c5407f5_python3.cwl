arguments:
- position: 25
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
- position: 28
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
    default: red
    inputBinding:
      position: 10
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default: 30
    inputBinding:
      position: 11
      prefix: --i_cz
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default: 5
    inputBinding:
      position: 12
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_13:
    default: 15
    inputBinding:
      position: 13
      prefix: --i_cz2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: 10
    inputBinding:
      position: 14
      prefix: --i_zr2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default: '0.065'
    inputBinding:
      position: 15
      prefix: --i_thetar2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_16:
    default: '0.41'
    inputBinding:
      position: 16
      prefix: --i_thetas2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_17:
    default: 16
    inputBinding:
      position: 17
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_18:
    default: 22
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default:
      class: File
      path: ../../data/boreholes/RN030982.csv
    inputBinding:
      position: 19
      prefix: --obs_gw
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
    default:
      class: File
      path: ../../data/boreholes/RN030983.csv
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/boreholes/RN030984.csv
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_howard.txt
    inputBinding:
      position: 22
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 23
      prefix: --pars
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default: 'True'
    inputBinding:
      position: 24
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_26:
    default: '.12'
    inputBinding:
      position: 26
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_27:
    default: 24
    inputBinding:
      position: 27
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_29:
    default: 5
    inputBinding:
      position: 29
      prefix: '-3'
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    inputBinding:
      position: 3
      prefix: --i2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: 0
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_31:
    default: 'True'
    inputBinding:
      position: 31
      prefix: --title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_32:
    default:
      class: File
      path: ../../data/VOM_soils/HowardSprings/soilprofile.par
    inputBinding:
      position: 32
      prefix: --soildata
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 33
      prefix: --obs_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 34
      prefix: --obs_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../data/fPAR/fpar_howard_v5.txt
    inputBinding:
      position: 35
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 36
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default: data/img/additonal_plots/howard_gw_sm_et_ass.png
    inputBinding:
      position: 37
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default: 'True'
    inputBinding:
      position: 4
      prefix: --depth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: s
    inputBinding:
      position: 5
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default: 2002
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_7:
    default: e
    inputBinding:
      position: 7
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default: 2007
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_9:
    default: VOM
    inputBinding:
      position: 9
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_37)
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
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/boreholes/RN030982.csv
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/boreholes/RN030983.csv
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/boreholes/RN030984.csv
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/DINGO_SWS/SWSCon_howard.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_32)
    entryname: data/VOM_soils/HowardSprings/soilprofile.par
    writable: false
  - entry: $(inputs.input_33)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_34)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_35)
    entryname: data/fPAR/fpar_howard_v5.txt
    writable: false
  - entry: $(inputs.input_36)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
