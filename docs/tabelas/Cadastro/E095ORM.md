# E095ORM

## Descrição

Cadastros - Fornecedores - Origem das Mercadorias

---

## Resumo

- Campos: 28
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFor | Number(009,0) | Não | Código do fornecedor |
| SeqOrm | Number(005,0) | Não | Sequência do endereço de origem da mercadoria |
| EndOrm | String(100) | Não | Endereço de origem da mercadoria |
| CplOrm | String(060) | Sim | Complemento de origem da mercadoria |
| PrxOrm | String(120) | Sim | Ponto de referência ou proximidade de origem da mercadoria |
| CepOrm | Number(008,0) | Sim | CEP do endereço de origem da mercadoria |
| IniOrm | Number(008,0) | Sim | Faixa inicial do CEP do endereço de origem da mercadoria |
| CidOrm | String(060) | Sim | Cidade do endereço de origem da mercadoria |
| EstOrm | String(002) | Sim | Estado do endereço de origem da mercadoria |
| InsOrm | String(025) | Sim | Inscrição estadual do endereço de origem da mercadoria |
| BaiOrm | String(075) | Sim | Bairro de origem da mercadoria |
| CgcOrm | Number(014,0) | Sim | Número do CNPJ de origem da mercadoria |
| DocIdeOrm | String(014) | Sim | Número do CNPJ de origem da mercadoria |
| SitOrm | String(001) | Não | Situação |
| EenOrm | String(018) | Sim | Código do endereço de origem da mercadoria |
| NumOrm | String(060) | Sim | Número do endereço de origem da mercadoria |
| TipOrm | String(001) | Sim | Tipo de Fornecedor |
| CodCli | Number(009,0) | Sim | Código do cliente |
| CodPrp | Number(009,0) | Sim | Código da propriedade |
| OriPor | String(001) | Sim | Origem da mercadoria do fornecedor provinda do porto |
| IndOba | Number(001,0) | Sim | Indicativo de Prestação de Serviços em Obra de Construção Civil |
| NroCno | String(014) | Sim | Número de inscrição do cadastro nacional de obra (CNO) |
| CodCae | Number(015,0) | Sim | Código do Cadastro de Atividade Econômica da Pessoa Física |
| PaiOrm | String(004) | Sim | Código do País da Origem das Mercadorias |
| TipEnd | Number(002,0) | Sim | Tipo do Endereço de Entrega |
| IndFtr | Number(001,0) | Sim | Indicativo da forma de tributação da contribuição previdenciária |
| DatIcp | Date | Sim | Data de Início de Vigência de Contribuição Previdenciária |
| DatFcp | Date | Sim | Data Final de Vigência de Contribuição Previdenciária |

---

## Chave Primária

- CodFor
- SeqOrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E095ORM_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

