# E000NFL

## Descrição

Tabelas - Integração - Notas de Entrada - Controle de integração folha do leite

---

## Resumo

- Campos: 26
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
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumInt | String(020) | Não | Número do Documento Externo (Integrado) |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| DatEnt | Date | Sim | Data da Entrada da Nota |
| DatEmi | Date | Sim | Data de emissão da nota fiscal de entrada |
| VlrBic | Number(015,2) | Sim | Soma dos valores base do ICMS dos itens de produtos da NF de entrada |
| VlrIcm | Number(015,2) | Sim | Soma dos valores do ICMS dos itens de produtos da NF de entrada |
| VlrBip | Number(015,2) | Sim | Soma dos valores base do IPI dos itens de produtos da NF de entrada |
| VlrIpi | Number(015,2) | Sim | Soma dos valores do IPI dos itens de produtos da NF de entrada |
| VlrBfu | Number(015,2) | Sim | Valor base do Funrural ou INSS dos itens de produto |
| VlrFun | Number(015,2) | Sim | Valor do Funrural ou INSS dos itens de produto |
| VlrBgi | Number(015,2) | Sim | Base de cálculo do GILRAT |
| VlrGil | Number(015,2) | Sim | Valor do GILRAT |
| VlrBsn | Number(015,2) | Sim | Valor base do Senar dos itens de produto |
| VlrSen | Number(015,2) | Sim | Valor do Senar dos itens de produto |
| VlrCcp | Number(015,2) | Sim | Valor da cota capital |
| SitDoc | Number(002,0) | Sim | Situação do documento eletrônico |
| SitNfc | String(001) | Não | Situação da nota fiscal de entrada |
| RetNfc | String(1000) | Sim | Retorno do Processamento |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E000NFLIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFor
- NumInt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
