# R038HTI

## Descrição

Histórico Times - OBSOLETA

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data da Início do Colaborador no Time |
| CodTim | String(008) | Não | Código do Time |
| DatTer | Date | Sim | Data do Término no Time |
| TipMtf | String(001) | Sim | Multifuncional |
| TipAhb | String(001) | Sim | Tipo de Atuação na Habilidade |
| CodCnc | String(001) | Sim | Conceito (Denso) |
| TotPon | Number(007,2) | Sim | Total de Pontos (Denso) |
| TimCer | String(001) | Sim | Time Certificado |
| DatCer | Date | Sim | Data da Certificação |
| TipCer | Number(001,0) | Sim | Tipo de Certificador |
| CadCer | Number(009,0) | Sim | Cadastro do Certificador |
| NotCer | Number(005,2) | Sim | Nota Média de Certificação |
| PerCer | Number(005,2) | Sim | %  Médio Certificação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- CodTim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HTI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HTI_004

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

