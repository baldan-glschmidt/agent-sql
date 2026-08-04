# E004PAD

## Descrição

Parâmetros - Geração automática de documentos eletrônicos

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| TipDoa | Number(002,0) | Sim | Tipo de documento automatizado |
| GerAut | String(001) | Sim | Indica se o documento será gerado de forma automática |
| FecAut | String(001) | Sim | Indica se o documento será fechado de forma automática |
| EmiAut | String(001) | Sim | Indica se o documento será Enviado de forma automática |
| CodSnf | String(003) | Sim | Código da série Padrão da nota fiscal de saída |
| ProAss | String(001) | Sim | Indica se o processamento será assíncrono, utilizando o processo automático XX |
| QtdGer | Number(002,0) | Sim | Quantidade Notas Geradas Por Execução |
| QtdDis | Number(002,0) | Sim | Quantidade Máxima de Disparos de uma Pendência |
| QtdSus | Number(003,0) | Sim | Quantidade de Dias que Pendências Concluídas Ficam Gravadas |
| QtdErr | Number(003,0) | Sim | Quantidade de Dias que Pendências Com Erros Ficam Gravadas |
| QtdDge | Number(002,0) | Sim | Quantidade de Dias de Espera para Processar as Pendências |
| MinRep | Number(003,0) | Sim | Quantidade de minutos para que uma pendência entre novamente na fila de processamento |
| TnsPad | String(005) | Sim | Transação de Produto Padrão para a geração do documento |
| TnsSad | String(005) | Sim | Transação de Serviço Padrão para a geração do documento |
| TipOpe | Number(001,0) | Sim | Tipo de operação |

---

## Chave Primária

- IdeUni

---

## Índices

### E004PADIndice2

**Tipo:** Não unico

Campos:
- CodEmp

### E004PADIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

### E004PADIndice4

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- TipDoa

### E004PADIndice5

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- TipDoa
- TipOpe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
