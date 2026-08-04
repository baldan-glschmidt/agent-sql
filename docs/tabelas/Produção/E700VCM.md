# E700VCM

## Descrição

Ficha - Modelo - Versões Componentes

---

## Resumo

- Campos: 34
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde o componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Não | Sequência lógica que o componente é utilizado na fabricação do Produto composto |
| DatAlt | Date | Não | Data Alteração para geração de versões p/ Custos |
| VerMod | String(015) | Não | Última versão do modelo na qual é incrementada em cada nova alteração |
| CodCmp | String(014) | Sim | Código do Componente (Produto) agregado |
| DesCmp | String(100) | Sim | Descrição complementar sobre a utilização do componente |
| VarDer | String(001) | Não | Derivação é Variável de um Produto p/ outro (deve ser ligado Produto X Modelo) |
| NecLig | String(001) | Sim | Componente Necessita ser ligado ao Produto específico que o utiliza |
| TipQtd | String(001) | Não | Tipo de Quantidade Utilizada (P=Proporcional - À Quantidade Base, F=Fixa - Ao Lote Técnico do Roteiro, R=Frequencial - À Quantidade Frequencial do Produto) |
| DtiVal | Date | Sim | Data de Validade inicial p/ utilização deste componente (Opcional) |
| DtfVal | Date | Sim | Data de Validade final p/ utilização deste componente (Opcional) |
| SeqSbs | Number(004,0) | Sim | Sequência para ser Substituída, conforme data de validade |
| SbsPro | String(014) | Sim | Utiliza este componente somente p/ o Produto Composto especificado |
| SbsCli | Number(009,0) | Sim | Usa este componente somente p/ o Cliente especificado (quando Pedido não for agrupado no Cálculo Necessidades) |
| CodGre | Number(009,0) | Sim | Usa este componente somente para o grupo de cliente especificado (quando pedido não for agrupado no cálculo necessidades) |
| IndPep | String(001) | Sim | Perda deste componente no Processo de fabricação é Individual ou Acumulada |
| IndEqi | String(001) | Não | Indicativo se o componente é equivalente ao relacionado ao campo "Substitui a Sequência" |
| ObsCmm | String(240) | Sim | Observações |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| DatGer | Date | Sim | Data de geração da versão |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica). |
| SelPro | String(001) | Não | Indica se o item será considerado para a área de manufatura (Nec. e Geração de OPs). |
| IndEos | String(001) | Sim | Componente é do tipo saída (consumo) ou entrada (originado de algum produto ou componente) |
| TipRdm | String(001) | Sim | Tipo de rendimento para o calculo da variação do consumo |
| VlrRdm | Number(014,5) | Sim | Valor do rendimento para ser aplicado a variação do consumo |
| CmpPen | String(001) | Sim | Parâmetro genérico para indicar se o componente é pendente ou não. |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o registro |
| HorGer | Number(005,0) | Sim | Hora da geração da versão |
| TolPes | Number(005,3) | Sim | % tolerância do peso líquido do produto ou do lote |
| FrmBxa | String(001) | Sim | Indica se a forma da baixa de componente será automática ou manual |
| CodClc | String(010) | Sim | Código da coleção |
| SeqVlc | Number(004,0) | Sim | Sequência da Validade da Coleção |

---

## Chave Primária

- CodEmp
- CodMod
- CodEtg
- SeqMod
- DatAlt
- VerMod

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700VCM_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

### IR_E700VCM_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

