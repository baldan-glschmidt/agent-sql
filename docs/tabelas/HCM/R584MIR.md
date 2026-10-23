# R584MIR

## Descrição

Manutenção do Inventário de Riscos

---

## Resumo

- Campos: 24
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| DesInv | String(100) | Não | Descrição do Inventário de Riscos |
| NomEst | String(060) | Sim | Nome do Estabelecimento |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição do Estabelecimento |
| NumCgc | Number(015,0) | Sim | Número de Inscrição do Estabelecimento - Obsoleto |
| CfjIns | String(014) | Sim | Número de Inscrição do Estabelecimento |
| CodCep | Number(008,0) | Sim | CEP do Estabecimento |
| TipLgr | String(005) | Sim | Tipo de Logradouro do Endereço do Estabelecimento |
| EndEst | String(040) | Sim | Endereço do Estabecimento |
| EndNum | String(006) | Sim | Número do Endereço do Estabelecimento |
| EndCpl | String(040) | Sim | Complemento do Endereço do Estabelecimento |
| NomBai | String(040) | Sim | Nome do Bairro |
| NomCid | String(040) | Sim | Nome da Cidade |
| SigEst | String(004) | Sim | UF do Estado |
| NomPai | String(040) | Sim | Nome do País |
| AtvEst | String(080) | Sim | Atividade econômica do estabelecimento |
| NmCnae | Number(007,0) | Sim | Código CNAE do estabelecimento |
| GraRis | Number(001,0) | Sim | Grau de risco do estabelecimento |
| DesInt | String(2000) | Sim | Introdução do inventário de riscos |
| DefCri | String(2000) | Sim | Definições e critérios de risco |
| CarEst | String(2000) | Sim | Caracterização do estabelecimento e unidades de trabalho |
| QtdCol | Number(009,0) | Sim | Quantidade de colaboradores no estabelecimento |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
