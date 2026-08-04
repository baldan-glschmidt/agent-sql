# E055DEP

## Descrição

Tributos - Débitos Especiais

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Sim | Data base |
| CodTns | String(005) | Não | Código da transação |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodSer | String(014) | Sim | Código do serviço |
| PerImp | Number(005,2) | Sim | Percentual imposto |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| LctCre | String(001) | Sim | Indicativo se o valor do imposto deverá ser considerado na coluna de créditos por entrada ou débitos por saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E055DEPindice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodImp
- DatBas
- CodTns
- CodPro
- CodDer
- CodSer
- CodDfs

---

## Relacionamentos

Nenhum relacionamento cadastrado.
