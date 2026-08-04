# E055ICM

## Descrição

Tributos - Parâmetros para geração da guia por código de arrecadação - ICMS

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatApi | Date | Não | Data base inicial de validade para a apuração |
| CodGri | Number(004,0) | Sim | Código da guia de recolhimento |
| CodTns | String(005) | Não | Código da transação |
| PagFor | Number(009,0) | Sim | Fornecedor padrão para gerar título de imposto a pagar no financeiro |
| PagTti | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| PagTri | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| DiaVct | Number(003,0) | Sim | Quantidade de dias após data apuração final para vencimento |
| AntPos | String(001) | Não | Indicativo do critério de definição de vencimento do imposto |
| CodPri | String(001) | Não | Código da periodicidade de apuração/cálculo do imposto |
| IniCon | Number(001,0) | Sim | Critério de início de contagem dos dias de vencimento |

---

## Chave Primária

- IdeUni

---

## Índices

### E055ICMIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodImp
- DatApi
- CodGri
- CodTns

---

## Relacionamentos

### IR_E055ICM_003

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

