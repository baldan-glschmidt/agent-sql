# R030ISE

## Descrição

Certificado de Isenção

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| ConCer | String(070) | Sim | Sigla e nome do Ministério ou Lei que concedeu o Certificado |
| NumCer | String(040) | Sim | Nro. Certificado Entidade, nro. portaria concessão, ou nro. lei específica |
| DatEmi | Date | Sim | Data de Emissão do Certificado/publicação da Lei |
| DatVen | Date | Sim | Data de Vencimento do Certificado |
| NumPro | String(040) | Sim | Número do protocolo de pedido de renovação |
| DatPro | Date | Sim | Data do protocolo de renovação |
| DatPub | Date | Sim | Data de publicação no Diário Oficial da União |
| PagPub | Number(005,0) | Sim | Nº da página no DOU ref. à publicação do documento de concessão do certificado |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ISE_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

