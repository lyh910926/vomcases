arguments:
- position: 27
  separate: true
  shellQuote: true
  valueFrom: --legend
- position: 28
  separate: true
  shellQuote: true
  valueFrom: --plot_cbar
- position: 31
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_timeseries.py
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
    default: s
    inputBinding:
      position: 17
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: 2006
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: e
    inputBinding:
      position: 19
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
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
    default: 2010
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_21:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 21
      prefix: --assobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/DINGO_QC/FcQ_howard.txt
    inputBinding:
      position: 22
      prefix: --assobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/DINGO_QC/FeQ_howard.txt
    inputBinding:
      position: 23
      prefix: --eobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 24
      prefix: --eobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/fPAR/fpar_howard_v5.txt
    inputBinding:
      position: 25
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 26
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default: c$_{rv}$ ($\mu$mol m$^3$ s$^{-1}$)
    inputBinding:
      position: 29
      prefix: --cblabel
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
    default: '3.0'
    inputBinding:
      position: 30
      prefix: --cbar_max
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_32:
    default: '.10'
    inputBinding:
      position: 32
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_33:
    default: '1.10'
    inputBinding:
      position: 33
      prefix: --yloc_title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_34:
    default: 24
    inputBinding:
      position: 34
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_35:
    default: RdYlGn
    inputBinding:
      position: 35
      prefix: --palette
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_36:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 36
      prefix: --stats_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 37
      prefix: --stats_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 38
      prefix: --stats_pc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_39:
    default: 7
    inputBinding:
      position: 39
      prefix: --moving_average
      separate: true
      shellQuote: true
    streamable: false
    type: int
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
  input_40:
    default:
    - MAE c$_{rv
    - 1.0}$
    inputBinding:
      itemSeparator: ','
      position: 40
      prefix: --stats_label
      separate: true
      shellQuote: true
    streamable: false
    type: string[]
  input_41:
    default: evaptot
    inputBinding:
      position: 41
      prefix: --var
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_42:
    default: asstot
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_43:
    default: pc
    inputBinding:
      position: 43
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_44:
    default: 10
    inputBinding:
      position: 44
      prefix: --ymax
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_45:
    default: '1.5'
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_46:
    default: 100
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_47:
    default: 0
    inputBinding:
      position: 47
      prefix: --ymin
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_48:
    default: 0
    inputBinding:
      position: 48
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_49:
    default: 0
    inputBinding:
      position: 49
      separate: true
      shellQuote: true
    streamable: false
    type: int
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
  input_50:
    default: 16
    inputBinding:
      position: 50
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_51:
    default: 15
    inputBinding:
      position: 51
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_52:
    default: 2
    inputBinding:
      position: 52
      prefix: --wpad
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_53:
    default: data/img/6_hs_fluxes.png
    inputBinding:
      position: 53
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
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
      glob: $(inputs.input_53)
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
    entryname: src_py/plot_timeseries.py
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
  - entry: $(inputs.input_21)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/DINGO_QC/FcQ_howard.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/DINGO_QC/FeQ_howard.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/fPAR/fpar_howard_v5.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/fPAR/dates_v5
    writable: false
  - entry: $(inputs.input_36)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_37)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_38)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
