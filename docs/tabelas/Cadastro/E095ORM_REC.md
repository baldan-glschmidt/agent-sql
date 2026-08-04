# E095ORM_REC

## Descrição

Cadastros - Recebimento de Documentos Eletrônicos - Fornecedores - Origem das Mercadorias

---

## Resumo

- Campos: 28
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| SeqOrm | Number(005,0) | Não | Sequência do endereço de origem da mercadoria |
| CodFor | Number(009,0) | Não | Código do fornecedor |
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
| IdeUni | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E095ORM_RECIndice1

**Tipo:** Não unico

Campos:
- DocIde
- SeqOrm

### E095ORM_RECIndice2

**Tipo:** Não unico

Campos:
- CgcCpf
- SeqOrm

---

## Relacionamentos

Nenhum relacionamento cadastrado.
