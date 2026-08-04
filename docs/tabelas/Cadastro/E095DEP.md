# E095DEP

## Descrição

Cadastros - Fornecedores - Dependentes

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodDpd | Number(009,0) | Não | Código do dependente |
| NomDep | String(100) | Não | Nome do dependente |
| CpfDep | Number(011,0) | Sim | Número do CPF do dependente |
| CodIde | String(010) | Sim | Documento de identidade do dependente |
| DatNas | Date | Não | Data de nascimento do dependente |
| EstCiv | Number(001,0) | Sim | Estado civil do dependente |
| GraPar | Number(001,0) | Não | Grau de parentesco do dependente |
| VlrPen | Number(015,2) | Sim | Valor da Pensão Judicial/Alimentícia |
| DatIni | Date | Sim | Data da validade inicial |
| DatFin | Date | Sim | Data da validade final |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| DesPar | String(030) | Sim | Descrição do Parentesco |

---

## Chave Primária

- CodFor
- CodDpd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E095DEP_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

