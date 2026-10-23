# R088IFR

## Descrição

Auto de Infrações de Trânsito

---

## Resumo

- Campos: 33
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatInf | Date | Não | Data da Infração |
| HorInf | Number(005,0) | Não | Hora da Infração |
| PlaVei | String(010) | Não | Placa do Veículo |
| EmpCon | Number(004,0) | Sim | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Sim | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Sim | Cadastro do Condutor |
| EndRua | String(080) | Sim | Endereço onde ocorreu a Infração |
| CodCid | Number(007,0) | Sim | Cidade onde ocorreu a Infração |
| DatPag | Date | Sim | Data do Pagamento da Infração |
| NumDoc | String(020) | Sim | Número do Documento |
| ValPag | Number(011,2) | Sim | Valor Pago pela Infração |
| DatRee | Date | Sim | Data do Reembolso da Infração |
| ValRee | Number(011,2) | Sim | Valor Reembolsado da Infração |
| DatDes | Date | Sim | Data do Desconto do Valor da Infração |
| QtdPar | Number(002,0) | Sim | Quantidade de Parcelas para o Desconto da Infração |
| ValDes | Number(011,2) | Sim | Valor Descontado da Infração |
| NumAit | String(020) | Sim | Número do Auto de Infração de Trânsito - AIT |
| DatInd | Date | Sim | Data da Indicação da Infração Cometida |
| DatLim | Date | Sim | Data Limite para Indicação da Infração Cometida |
| NomInd | String(040) | Sim | Nome da Indicação da Infração Cometida |
| CodOrE | Number(002,0) | Sim | Código do Órgão Emissor |
| DatExp | Date | Sim | Data de Expedição |
| DatRec | Date | Sim | Data de Recebimento |
| CodCli | Number(008,0) | Sim | Código do Cliente |
| DatVen | Date | Sim | Data Vencimento |
| ResPag | Number(001,0) | Sim | Responsável pelo Pagamento |
| ObsIfr | String(2500) | Sim | Observação da Infração |
| TipTpa | Number(001,0) | Sim | Tipo de Via em que Ocorreu o Acidente |
| TemRec | String(001) | Sim | Houve Recurso (S/N) |
| RecDef | String(001) | Sim | O Recurso foi Deferido (S/N) |
| ComCon | String(001) | Sim | Comunica Infrator (S/N) |
| EccIfr | String(254) | Sim | Endereço Cópia do E-mail para Comunicação à Terceiros |
| StaEma | String(001) | Sim | E-mail enviado (S/N) |

---

## Chave Primária

- DatInf
- HorInf
- PlaVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
