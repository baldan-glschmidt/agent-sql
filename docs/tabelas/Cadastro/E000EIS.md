# E000EIS

## Descrição

Tabelas - Integrações - Exceções de Integração com Sistemas Terceiros

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código da Integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| TipEis | Number(001,0) | Não | Tipo de exceção ocorrida |
| SeqEis | Number(009,0) | Não | Sequencia da exceção de integração |
| CodMot | Number(004,0) | Sim | Código do motivo da exceção |
| DesMot | String(999) | Sim | Descrição da Exceção |
| DatGer | Date | Sim | Data da geração da exceção |
| HorGer | Number(005,0) | Sim | Hora da geração da exceção |
| IdtReq | String(020) | Sim | Identificação da requisição do web service |
| IdtReg | String(020) | Sim | Identificação do registro na requisição |

---

## Chave Primária

- CodInt
- CodEmp
- CodFil
- TipEis
- SeqEis

---

## Índices

### E000EISIndice1

**Tipo:** Não unico

Campos:
- CodInt
- CodEmp
- CodFil
- TipEis
- IdtReg

### E000EISIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E000EIS_000

**Tabela:** E000SIS

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

### IR_E000EIS_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000EIS_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

