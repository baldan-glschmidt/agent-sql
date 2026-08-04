# E085SPR

## Descrição

Cadastros - Clientes - Propriedades - Subpropriedades

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodPrp | Number(009,0) | Não | Código da propriedade |
| CodSpr | Number(009,0) | Não | Código da Subpropriedade |
| NomSpr | String(100) | Não | Nome da Subpropriedade |
| ArrPrp | String(001) | Sim | Indicativo de arrendamento da propriedade |
| TipArp | Number(001,0) | Sim | Tipo do Arrendamento da Propriedade |
| ObsPrp | String(1999) | Sim | Observações da Subpropriedade |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodCli
- CodPrp
- CodSpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
