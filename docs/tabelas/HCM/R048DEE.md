# R048DEE

## Descrição

Definições da Contabilização

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| OriCon | Number(001,0) | Sim | Origem das contas |
| ConRat | String(001) | Sim | Considerar os rateios da origem das contas |
| UsaNat | String(001) | Sim | Usa Natureza Despesa (S,N) |
| UsaRat | String(001) | Sim | Usa Rateio Gerencial  (S,N,C) |
| IncFer | String(001) | Sim | Incluir Férias (S,N) |
| IncRes | String(001) | Sim | Incluir Rescisões (S,N) |
| InsSep | String(001) | Sim | Acumular INSS separados (S,N) |
| InsTer | String(001) | Sim | Separar INSS Parte Empresa de Colaboradores e Terceiros |
| ConZer | String(001) | Sim | Listar Contas Zeradas (S,N) |
| LitPvn | String(001) | Sim | Ponto, Virgula ou Nenhum |
| TruZer | String(001) | Sim | Truncar Zeros a Esquerda (S,N) |
| SomCon | String(001) | Sim | Somar Contas Iguais |
| LayHea | String(350) | Sim | LayOut Header do Arquivo - Saia do campo c/ TAB |
| LayHec | String(350) | Sim | LayOut Header p/ C.Custo - Saia do campo c/ TAB |
| LayLan | String(350) | Sim | LayOut Lançamentos - Saia do campo c/ TAB |
| LayTot | String(350) | Sim | LayOut Lançamentos Totais - Saia do campo c/ TAB |
| LayGer | String(350) | Sim | LayOut Lançamentos Gerenciais - Saia do campo c/ TAB |
| LayTra | String(350) | Sim | Layout Trailler Arquivo - Saia do campo c/ TAB |
| LayTrc | String(350) | Sim | Layout Trailler do Centro de Custo - Saia do campo c/ TAB |
| ParDob | String(001) | Sim | Partidas Dobradas |
| CCuCon | String(001) | Sim | C.Custo na Conta Contábil |
| BraDir | String(001) | Sim | Preencher com Brancos à Direita dos Valores Numéricos |
| GerTab | String(001) | Sim | Gerar Dados nas Tabelas Auxiliares |
| RegTab | Number(003,0) | Sim | Regra Alteração Para as Tabelas R048CON e R048DCC |
| IncPpj | String(001) | Sim | Incluir Pagto P.Jurídica |
| IncPpf | String(001) | Sim | Incluir Pagto P.Física |
| RegCtb | Number(003,0) | Sim | Regra Alteração R048CTB |
| LinSAP | Number(004,0) | Sim | Quantidade máxima de registros por lote de paginação |
| QtdLot | Number(006,0) | Sim | Quantidade de registros para gravação em lote |
| AgrCpl | String(001) | Sim | Agrupar Complemento Histórico |
| IncAnp | String(001) | Sim | Incluir Avulso Não Portuário (S,N) |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
