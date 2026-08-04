# E081FPG

## Descrição

Tabelas - Atributos da Venda - Condições - Formas de Pagamentos

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdcFpg | Number(009,0) | Não | Índice da forma de pagamento na condição do atributo de venda |
| IdcIac | Number(009,0) | Não | Índice das condições do atributo de venda |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(009,0) | Sim | Usuário responsável pela última alteração do registro |
| ObsFpg | String(099) | Sim | Observação da forma de pagamento na condição do atributo de venda |
| SitReg | String(001) | Não | Situação da forma de pagamento na condição do atributo de venda |

---

## Chave Primária

- IdcFpg

---

## Índices

### E081FPG_UNIQUE

**Tipo:** Unico

Campos:
- IdcIac
- CodFpg

---

## Relacionamentos

Nenhum relacionamento cadastrado.
