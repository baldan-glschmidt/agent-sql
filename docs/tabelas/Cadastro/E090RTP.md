# E090RTP

## Descrição

Cadastros - Representantes - Ligação Representante X Tabela de Preços

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| CodMar | String(010) | Não | Código da Marca/Etiqueta vinculada a um produto ou a um pedido |
| EmpTpr | Number(004,0) | Não | Código da empresa da Tabela de Preço |
| CodTpr | String(004) | Não | Código da tabela de preço |
| SitLrt | String(001) | Sim | Situação da ligação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodRep
- CodMar
- EmpTpr
- CodTpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
