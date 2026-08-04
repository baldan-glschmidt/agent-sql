# E075PCD

## Descrição

Cadastros - Preço de custo por produto e derivação

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
| DatIni | Date | Não | Data Inicial do período |
| DatFim | Date | Não | Data final do período |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodFam | String(006) | Sim | Código da família de produto |
| PreCus | Number(015,10) | Sim | Preço de custo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E075PCDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- DatIni
- DatFim
- CodPro
- CodDer
- CodFam

---

## Relacionamentos

Nenhum relacionamento cadastrado.
