# E085PRO

## Descrição

Cadastros - Clientes - Propriedades

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodPrp | Number(009,0) | Não | Código da propriedade |
| NomPrp | String(100) | Não | Nome da propriedade |
| ArrPrp | String(001) | Sim | Indicativo de arrendamento da propriedade |
| TipArp | Number(001,0) | Sim | Tipo do Arrendamento da Propriedade |
| CliPrp | Number(009,0) | Sim | Código do cliente que representa a propriedade |
| ObsPrp | String(1999) | Sim | Observações da propriedade |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodInd | Number(012,0) | Sim | Código da propriedade junto ao INDEA |

---

## Chave Primária

- CodCli
- CodPrp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
