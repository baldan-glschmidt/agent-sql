# E066OPE

## Descrição

Cadastros - Operadoras Cartões de Débito/Crédito

---

## Resumo

- Campos: 32
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOpe | Number(004,0) | Não | Código da operadora |
| NomOpe | String(100) | Não | Nome da operadora |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF da operadora |
| DocIdeOpe | String(014) | Sim | Número do CNPJ ou CPF da operadora |
| InsEst | String(025) | Sim | Inscrição estadual da operadora |
| CodSuf | String(010) | Sim | Número da operadora junto à Suframa |
| CepOpe | Number(008,0) | Sim | CEP da operadora |
| EndOpe | String(100) | Sim | Endereço da operadora |
| NenOpe | String(060) | Sim | Número do endereço da operadora |
| CplEnd | String(200) | Sim | Complemento do endereço da operadora (sala, andar, etc.) |
| BaiOpe | String(075) | Sim | Bairro da operadora |
| CidOpe | String(060) | Sim | Cidade da operadora |
| SigUfs | String(002) | Sim | Sigla do estado da operadora |
| CodPai | String(004) | Sim | Código do país da operadora |
| SitOpe | String(001) | Não | Situação da operadora |
| CliFat | Number(009,0) | Sim | Código do cliente relacionado ao cadastro da operadora |
| QtdDpr | Number(003,0) | Sim | Intervalo de dias entre a venda e o primeiro repasse (Crédito) |
| QtdDdp | Number(003,0) | Sim | Intervalo de dias entre o primeiro repasse e as demais parcelas de repasse(C) |
| OpeTrv | String(001) | Sim | Indicativo se a operadora trabalha com resumo de venda anterior a conciliação |
| OpeLio | Number(005,0) | Sim | Código layout de importação para conciliação operadora de cartão de crédito |
| OpeCab | String(004) | Sim | Código do registro do cabeçalho do arquivo retorno da conciliação |
| OpeRod | String(004) | Sim | Código do registro do rodapé do arquivo retorno da conciliação |
| OpeLvo | Number(005,0) | Sim | Código layout de importação das vendas para operadora de cartão de crédito |
| OpeCbr | String(004) | Sim | Código do registro do cabeçalho do arquivo retorno do registro de vendas |
| OpeRdr | String(004) | Sim | Código do registro do rodapé do arquivo retorno do registro de vendas |
| OpeCco | String(014) | Sim | Número da conta interna onde será realizado o depósito pela operadora |
| OpeDir | String(250) | Sim | Diretório padrão para arquivos de retorno para conciliação operadoras cartão |
| QtdDpd | Number(003,0) | Sim | Intervalo de dias entre a venda e o repasse (débito) |
| PerRpd | Number(005,2) | Sim | Taxa de repasse (em percentual) cobrado pela administradora de cartão |
| IndPos | Number(001,0) | Não | Indicativo dos tipos de recebimentos por POS |
| InsTef | String(150) | Sim | Código da instituição para o TEF |
| DifPar | Number(001,0) | Não | Indicativo de como aplicar o valor da diferença resultado da divisão de parcelas |

---

## Chave Primária

- CodOpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
