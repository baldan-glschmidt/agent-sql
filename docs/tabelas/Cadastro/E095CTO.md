# E095CTO

## Descrição

Cadastros - Fornecedores - Contatos

---

## Resumo

- Campos: 23
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| SeqCto | Number(005,0) | Não | Sequência de contato |
| NomCto | String(150) | Não | Nome da pessoa de contato no fornecedor |
| DatNas | Date | Sim | Data do nascimento do contato |
| NivCto | String(001) | Sim | (descontinuado) Nível da pessoa de contato do fornecedor |
| SetCto | String(030) | Sim | Setor da pessoa de contato |
| CarCto | String(050) | Sim | Cargo da pessoa de contato do fornecedor |
| FonCto | String(020) | Sim | Número do telefone da pessoa de contato |
| RamCto | Number(004,0) | Sim | Número do ramal da pessoa de contato |
| FaxCto | String(020) | Sim | Número do FAX da pessoa de contato |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| HobCon | String(015) | Sim | Hobby do Contato |
| TimCon | String(015) | Sim | Time do Contato |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| SitCto | String(001) | Sim | Situação do registro |
| CpfCto | Number(012,0) | Sim | CPF do contato |
| CodNiv | Number(004,0) | Sim | Código do Nível |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodFor
- SeqCto

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E095CTO_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

