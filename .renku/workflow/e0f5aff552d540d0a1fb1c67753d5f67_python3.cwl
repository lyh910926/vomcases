arguments:
- position: 35
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
- position: 38
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
      path: ../../src_py/plot_gw_sm.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: s
    inputBinding:
      position: 10
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default: 2002
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default: e
    inputBinding:
      position: 12
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: 2007
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: VOM
    inputBinding:
      position: 14
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default: red
    inputBinding:
      position: 15
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_16:
    default: 30
    inputBinding:
      position: 16
      prefix: --i_cz
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_17:
    default: 5
    inputBinding:
      position: 17
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_18:
    default: 15
    inputBinding:
      position: 18
      prefix: --i_cz2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: 5
    inputBinding:
      position: 19
      prefix: --i_zr2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
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
    default: '0.065'
    inputBinding:
      position: 20
      prefix: --i_thetar2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_21:
    default: '0.41'
    inputBinding:
      position: 21
      prefix: --i_thetas2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default: 16
    inputBinding:
      position: 22
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_23:
    default: 28
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_24:
    default:
      class: File
      path: ../../data/boreholes/RN030982.csv
    inputBinding:
      position: 24
      prefix: --obs_gw
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/boreholes/RN030983.csv
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/boreholes/RN030984.csv
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_howard.txt
    inputBinding:
      position: 27
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_litch.txt
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_adelaide.txt
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_daly.txt
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_dry.txt
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_32:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_sturt.txt
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 33
      prefix: --pars
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default: 'True'
    inputBinding:
      position: 34
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_36:
    default: '.12'
    inputBinding:
      position: 36
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_37:
    default: 24
    inputBinding:
      position: 37
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_39:
    default: 5
    inputBinding:
      position: 39
      prefix: '-3'
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default: 0
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_41:
    default: 'True'
    inputBinding:
      position: 41
      prefix: --title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_42:
    default:
      class: File
      path: ../../data/VOM_soils/HowardSprings/soilprofile.par
    inputBinding:
      position: 42
      prefix: --soildata
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_43:
    default:
      class: File
      path: ../../data/VOM_soils/Litchfield/soilprofile.par
    inputBinding:
      position: 43
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_44:
    default:
      class: File
      path: ../../data/VOM_soils/AdelaideRiver/soilprofile.par
    inputBinding:
      position: 44
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_45:
    default:
      class: File
      path: ../../data/VOM_soils/DalyUncleared/soilprofile.par
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_46:
    default:
      class: File
      path: ../../data/VOM_soils/DryRiver/soilprofile.par
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_47:
    default:
      class: File
      path: ../../data/VOM_soils/SturtPlains/soilprofile.par
    inputBinding:
      position: 47
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_48:
    default: data/img/5_gw_sm.png
    inputBinding:
      position: 48
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    inputBinding:
      position: 8
      prefix: --i2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: 'True'
    inputBinding:
      position: 9
      prefix: --depth
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_48)
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
    entryname: src_py/plot_gw_sm.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/boreholes/RN030982.csv
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/boreholes/RN030983.csv
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/boreholes/RN030984.csv
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/DINGO_SWS/SWSCon_howard.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/DINGO_SWS/SWSCon_litch.txt
    writable: false
  - entry: $(inputs.input_29)
    entryname: data/DINGO_SWS/SWSCon_adelaide.txt
    writable: false
  - entry: $(inputs.input_30)
    entryname: data/DINGO_SWS/SWSCon_daly.txt
    writable: false
  - entry: $(inputs.input_31)
    entryname: data/DINGO_SWS/SWSCon_dry.txt
    writable: false
  - entry: $(inputs.input_32)
    entryname: data/DINGO_SWS/SWSCon_sturt.txt
    writable: false
  - entry: $(inputs.input_33)
    entryname: work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_42)
    entryname: data/VOM_soils/HowardSprings/soilprofile.par
    writable: false
  - entry: $(inputs.input_43)
    entryname: data/VOM_soils/Litchfield/soilprofile.par
    writable: false
  - entry: $(inputs.input_44)
    entryname: data/VOM_soils/AdelaideRiver/soilprofile.par
    writable: false
  - entry: $(inputs.input_45)
    entryname: data/VOM_soils/DalyUncleared/soilprofile.par
    writable: false
  - entry: $(inputs.input_46)
    entryname: data/VOM_soils/DryRiver/soilprofile.par
    writable: false
  - entry: $(inputs.input_47)
    entryname: data/VOM_soils/SturtPlains/soilprofile.par
    writable: false
successCodes: []
temporaryFailCodes: []
