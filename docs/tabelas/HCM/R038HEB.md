# R038HEB

## Descrição

Histórico Estabilidade

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| IniEtb | Date | Não | Data de Início da Estabilidade |
| FimEtb | Date | Sim | Data Final da Estabilidade |
| CodEtb | Number(002,0) | Sim | Código da Estabilidade |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| OriEst | Number(001,0) | Sim | Origem da Estabilidade |
| ObsIni | String(255) | Sim | Observação Início |
| ObsFim | String(255) | Sim | Observação Fim |
| IniAfa | Date | Sim | Data Início Afastamento/Suspensão |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniEtb

---

## Índices

### R038HEBIndice2

**Tipo:** Não unico

Campos:
- StaAtu
- IniEtb

### R038HEBIndice3

**Tipo:** Não unico

Campos:
- StaAtu
- FimEtb

---

## Relacionamentos

### IR_R038HEB_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

