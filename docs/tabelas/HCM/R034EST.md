# R034EST

## Descrição

Informações do estrangeiro

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatChe | Date | Sim | Data de chegada ao Brasil |
| VisEst | Number(002,0) | Sim | Classificação da condição do estrangeiro no Brasil |
| RegEst | String(014) | Sim | Carteira de Estrangeiro |
| EmiEst | String(020) | Sim | Órgão emissor do registro de estrangeiro |
| DatEst | Date | Sim | Data de expedição do registro de estrangeiro |
| DvlEst | Date | Sim | Data de Validade da Carteira de Estrangeiro |
| DvlCtp | Date | Sim | Data de Validade da Carteira de Trabalho (Estrangeiro) |
| CasBra | String(001) | Sim | Casado com Brasileiro |
| FilCbr | String(001) | Sim | Filhos Brasileiros |
| NumPor | String(016) | Sim | Número da Portaria de Naturalização |
| DatPor | Date | Sim | Data de Naturalização |
| TmpRes | Number(001,0) | Sim | Tempo de residência do trabalhador imigrante |
| DatTer | Date | Sim | Data de término da residência do trabalhador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
