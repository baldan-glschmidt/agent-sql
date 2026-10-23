# R038HPO

## Descrição

Histórico Postos de trabalho

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IniAtu | Date | Não | Início da atuação do Colaborador no Posto de trabalho |
| SeqHis | Number(002,0) | Não | Sequência do Histórico |
| CodTap | Number(003,0) | Sim | Define qual Tipo de atuação o Colaborador exercerá no seu Posto |
| MotAlt | Number(003,0) | Sim | Motivo de alteração do Posto de Trabalho |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho em que o Colaborador atuará |
| TerAtu | Date | Sim | Término da atuação do Colaborador no Posto de trabalho |
| ObsHpo | String(700) | Sim | Observação do histórico de posto de trabalho |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| TipSbs | Number(001,0) | Sim | Tipo de Substituído |
| CadSbs | Number(009,0) | Sim | Cadastro de Substituído |
| PerAdi | Number(009,5) | Sim | Percentual de Adicional de Posto |
| FunEso | String(001) | Sim | Função eSocial |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniAtu
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HPO_005

**Tabela:** R017TAP

| Origem | Destino |
|--------|---------|
| CodTap | CodTap |

### IR_R038HPO_006

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| MotAlt | CodMot |

### IR_R038HPO_008

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

