# R038HCH

## Descrição

Histórico de Crachás de Colaboradores

---

## Resumo

- Campos: 18
- Chave Primária: 6 campo(s)
- Índices: 5
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
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
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| CraEnt | String(001) | Sim | Crachá provisório entregue |
| CodMSO | Number(002,0) | Sim | Motivo solicitação do provisório |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |

---

## Chave Primária

- TipCra
- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

### R038HCHIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatIni
- HorIni

### R038HCHIndice3

**Tipo:** Não unico

Campos:
- NumCad

### R038HCHIndice4

**Tipo:** Não unico

Campos:
- StaAtu
- DatIni
- HorIni
- DatFim
- HorFim

### R038HCHIndice5

**Tipo:** Não unico

Campos:
- StaAtu
- DatFim
- HorFim

### R038HCHIndice6

**Tipo:** Não unico

Campos:
- TipCra
- TipCol
- NumEmp
- NumCad
- DatIni
- HorIni

---

## Relacionamentos

### IR_R038HCH_003

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

