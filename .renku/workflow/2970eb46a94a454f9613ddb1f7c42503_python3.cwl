arguments:
- position: 19
  separate: true
  shellQuote: true
  valueFrom: --legend
- position: 28
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
      path: ../../data/DINGO_QC/FeQ_dry.txt
    inputBinding:
      position: 10
      prefix: --eobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 11
      prefix: --eobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default: red
    inputBinding:
      position: 12
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: black
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_14:
    default: green
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default:
      class: File
      path: ../../data/fPAR/fpar_dry_v5.txt
    inputBinding:
      position: 15
      prefix: --pcobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 16
      prefix: --pcobsdates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default: predicted roots
    inputBinding:
      position: 17
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default: prescribed roots
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
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
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 20
      prefix: --stats_evap
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/evap_beststats.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 22
      prefix: --stats_ass
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/ass_beststats.txt
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 24
      prefix: --stats_pc
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/pc_beststats.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default: MAE predicted
    inputBinding:
      position: 26
      prefix: --stats_label
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_27:
    default: MAE prescribed
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: '.10'
    inputBinding:
      position: 29
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_best/results_daily.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: '1.10'
    inputBinding:
      position: 30
      prefix: --yloc_title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default: 24
    inputBinding:
      position: 31
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_32:
    default: 7
    inputBinding:
      position: 32
      prefix: --moving_average
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_33:
    default: evaptot
    inputBinding:
      position: 33
      prefix: --var
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_34:
    default: asstot
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_35:
    default: pc
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_36:
    default: 10
    inputBinding:
      position: 36
      prefix: --ymax
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_37:
    default: '1.5'
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_38:
    default: 100
    inputBinding:
      position: 38
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_39:
    default: 0
    inputBinding:
      position: 39
      prefix: --ymin
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default: s
    inputBinding:
      position: 4
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_40:
    default: 0
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_41:
    default: 0
    inputBinding:
      position: 41
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_42:
    default: 16
    inputBinding:
      position: 42
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_43:
    default: 15
    inputBinding:
      position: 43
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_44:
    default: data/img/11_zr_dry.png
    inputBinding:
      position: 44
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: 2008
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
    default: 2013
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 8
      prefix: --assobs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/DINGO_QC/FcQ_dry.txt
    inputBinding:
      position: 9
      prefix: --assobs_qc
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_44)
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
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/DINGO/GPPdaily_dry.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/DINGO_QC/FcQ_dry.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO_QC/FeQ_dry.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO/Ea_dry.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/fPAR/fpar_dry_v5.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/fPAR/dates_v5
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/evap_beststats.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/ass_beststats.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_stats_best/pc_beststats.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/VOM_output/additional_analyses/fixed_roots/DryRiver/sce_stats_best/pc_beststats.txt
    writable: false
successCodes: []
temporaryFailCodes: []
