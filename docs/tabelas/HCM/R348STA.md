# R348STA

## Descrição

eSocial - GRFGTS - Status das solicitações - obsoleta

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| TipPen | Number(002,0) | Sim | Tipo da solicitação |
| StaSit | Number(002,0) | Sim | Situação da solicitação |
| DesRes | String(250) | Sim | Resumo da solicitação |
| DatHor | Number(014,6) | Sim | Data/Hora da solicitação |
| CodUsu | Number(010,0) | Sim | Usuário solicitante |
| NumRec | String(040) | Sim | Recibo de retorno |
| DesRet | String(2000) | Sim | Descrição do retorno |
| UltRet | Number(014,6) | Sim | Data/Hora do último retorno |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| NumIns | Number(015,0) | Sim | Número de inscrição do empregador |
| CfjIns | String(014) | Sim | Número de inscrição do empregador |

---

## Chave Primária

- IdePen

---

## Índices

### R348STAIndice1

**Tipo:** Não unico

Campos:
- DatHor

---

## Relacionamentos

Nenhum relacionamento cadastrado.
