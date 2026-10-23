# R064TSR

## Descrição

Troca de Serviço

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Troca de Serviço |
| DatFim | Date | Sim | Data Final da Troca de Serviço |
| CodSRv | Number(004,0) | Sim | Código do Serviço |
| CodTSe | Number(002,0) | Sim | Turno de Serviço |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064TSR_005

**Tabela:** R005SRV

| Origem | Destino |
|--------|---------|
| CodSRv | CodSrv |

### IR_R064TSR_006

**Tabela:** R005TUR

| Origem | Destino |
|--------|---------|
| CodSRv | CodSrv |
| CodTSe | CodTSe |

