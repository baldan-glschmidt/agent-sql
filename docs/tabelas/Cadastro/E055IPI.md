# E055IPI

## Descrição

Tributos - Parâmetros para geração da guia por código de arrecadação - IPI

---

## Resumo

- Campos: 15
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
| CodPro | String(014) | Sim | Código do produto |
| CodSer | String(014) | Sim | Código do serviço |
| PagFor | Number(009,0) | Sim | Fornecedor padrão para gerar título de imposto a pagar no financeiro |
| PagTti | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| PagTri | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E055IPIIndice1

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

### IR_E055IPI_003

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

