# R070HCH

## Descrição

Histórico de Crachás Outras Unidades

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 4
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatIni | Date | Não | Data de Início do Uso do Crachá |
| HorIni | Number(005,0) | Não | Hora de Início do Uso do Crachá |
| ViaCra | Number(002,0) | Sim | Número da Via do Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| RecEPr | String(030) | Sim | Recibo da Entrega do Provisório |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Crachá |

---

## Chave Primária

- TipCra
- NumEmp
- NumCad
- DatIni
- HorIni

---

## Índices

### R070HCHIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatIni
- HorIni

### R070HCHIndice3

**Tipo:** Não unico

Campos:
- NumCad

### R070HCHIndice4

**Tipo:** Não unico

Campos:
- StaAtu
- DatIni
- HorIni

### R070HCHIndice5

**Tipo:** Não unico

Campos:
- StaAtu
- DatFim
- HorFim

---

## Relacionamentos

### IR_R070HCH_002

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

