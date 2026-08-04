# E030BAN

## Descrição

Cadastros - Bancos

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| NomBan | String(100) | Não | Nome do banco |
| AbrBan | String(010) | Não | Sigla do banco |
| PatLiq | Number(015,2) | Sim | Patrimônio líquido do banco |
| DatPat | Date | Sim | Data patrimônio líquido do banco |
| CatBan | String(001) | Sim | Categoria do banco |
| TipBan | Number(001,0) | Sim | Tipo do banco |
| PerApl | Number(005,2) | Sim | Percentual de aplicações financeiras em relação ao patrimônio |
| ExiNlo | String(001) | Sim | Pagamento eletrônico exige novo lote para FGTS |
| PerCom | Number(005,2) | Sim | Percentual de comissão a ser cobrada do banco |
| DatRep | Date | Sim | Data do repasse da comissão pelo banco |
| QtdRev | Number(009,0) | Sim | Quantidade de parcelas para repasse ao vendedor |
| QtdRef | Number(009,0) | Sim | Quantidade de parcelas para repasse a filial |
| CodCli | Number(009,0) | Sim | Código do banco como cliente |
| CodFor | Number(009,0) | Sim | Código do fornecedor relacionado ao cadastro do banco |
| FgtSeg | String(001) | Sim | Segmento para exportar FGTS no pagamento eletrônico |
| GpsSeg | String(001) | Sim | Segmento para exportar GPS no pagamento eletrônico |
| BanTef | String(020) | Sim | Banco identificado pelo TEF |
| BanBol | String(005) | Sim | Código do banco para emissão do boleto bancário |
| LogBan | String(040) | Sim | Nome do arquivo com a logomarca do banco para emissão do boleto |
| PerRep | Number(005,2) | Sim | Percentual de comissão a ser paga ao representantes |
| MinTed | Number(015,2) | Sim | Valor mínimo para que o tipo de pagamento seja TED |
| MinJ52 | Number(015,2) | Sim | Valor mínimo para geração de registro J52 no pagamento eletrônico |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ do banco |
| DocIdeBan | String(014) | Sim | Número do CNPJ do banco |
| PtoSeg | String(001) | Sim | Segmento para exportar PT/PO no pagamento eletrônico |
| IdeSpb | String(008) | Sim | Identificador de Sistema de Pagamentos Brasileiro - ISPB |

---

## Chave Primária

- CodBan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
