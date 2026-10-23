# R191RES

## Descrição

Objetivos Coletivos - Objetivos - Notas

---

## Resumo

- Campos: 28
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência |
| IdeObj | Number(006,0) | Não | Identificação do objetivo coletivo |
| DesObj | String(2000) | Sim | Descrição do objetivo coletivo |
| SeqObj | Number(006,0) | Sim | Sequência do objetivo coletivo |
| PriObj | Number(003,0) | Sim | Prioridade do objetivo coletivo |
| PesObj | Number(005,2) | Sim | Peso do objetivo coletivo |
| TipRes | Number(001,0) | Sim | Tipo do resultado do objetivo coletivo |
| NotObj | Number(016,4) | Sim | Resultado da avaliação do objetivo coletivo |
| PerObj | Number(014,2) | Sim | % atingido na avaliação do objetivo coletivo |
| VlrSt1 | Number(016,4) | Sim | Valor do step mínimo |
| VlrSt2 | Number(016,4) | Sim | Valor do step target |
| VlrSt3 | Number(016,4) | Sim | Valor do step máximo |
| DirObj | Number(001,0) | Sim | Direção para avaliação do objetivo coletivo |
| DesInd | String(300) | Sim | Descrição de orientação do indicador |
| DesMet | String(300) | Sim | Descrição de orientação das metas |
| DesRes | String(2000) | Sim | Descrição do resultado do objetivo coletivo |
| ComChe | String(1500) | Sim | Comentário do avaliador que justifica a nota |
| SitObj | Number(001,0) | Sim | Situação do Objetivo |
| LimMin | Number(005,2) | Sim | Limite mínimo para ser considerado na apuração do resultado |
| LimMax | Number(005,2) | Sim | Limite máximo para ser considerado na apuração do resultado |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da evidência da competência |
| CodCPr | String(010) | Sim | Conceito avaliado para a evidência da competência |
| LanRes | Number(001,0) | Sim | Forma de lançamento do resultado na avaliação individual |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- IdeObj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R191RES_005

**Tabela:** R191AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |

