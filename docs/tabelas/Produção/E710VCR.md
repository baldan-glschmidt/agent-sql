# E710VCR

## Descrição

Ficha - Roteiro - Versões Seqüências Operações

---

## Resumo

- Campos: 33
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodRot | String(014) | Não | Código do Roteiro de Produção associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção para execução da Operação |
| SfxEtr | Number(003,0) | Não | Opção do Estágio (1=Padrão, 2-999=Alternativas) |
| SeqRot | Number(004,0) | Não | Seqüência lógica da Operação no Roteiro de Produção |
| SfxSeq | Number(002,0) | Não | Opção da seqüência (1=Padrão, 2-99=Alternativas) |
| DatAlt | Date | Não | Data de Alteração da seqüência válida p/ Custos |
| CodOpr | String(006) | Sim | Código da operação |
| UtiOpr | String(001) | Não | Tempo automático do cad. operações (tempo da operação vale p/ roteiros que utilizam tempo automático) |
| CodCre | String(008) | Sim | Código do Centro de Recurso onde a operação é executada |
| TmpPrp | Number(010,4) | Sim | Tempo Proporcional utilizado p/ execução da operação (Unidade tempo do C. Recurso) |
| TmpFix | Number(010,4) | Sim | Tempo fixo. Set-Up na operação (Unidade de Tempo do C. Recurso) |
| TmpFrq | Number(012,3) | Sim | Tempo Freqüencial em Função da quantidade freqüencial |
| QtdFrq | Number(014,5) | Sim | Quantidade para dimensionar o tempo freqüencial |
| UniCre | String(001) | Não | Unidade de Medida de Tempo (M=Minuto, S=Segundo, D=Dia, H=Hora) |
| CodSer | String(014) | Sim | Código do serviço (Quando operação é realizada por Terceiros) |
| CodFor | Number(009,0) | Sim | Código Fornecedor (Quando operação é realizada por Terceiros) |
| CodCcu | String(009) | Sim | Código do Centro de Custos |
| DatGer | Date | Sim | Data geração de versão |
| CodCel | String(004) | Sim | Código da Célula de Produção (Grupos de Trabalho) |
| TipPos | Number(001,0) | Não | Posicionamento (1=Inicia após fim do anterior, 2=inicia junto, 3=finaliza junto) |
| PerSbr | Number(003,0) | Sim | Percentual de sobreposição da operação em relação a operação precedente (quando tipo posicionamento = 2) |
| MovOrp | String(001) | Não | Indica se é controlado através de movimento (apontamento) por Ordens de Produção |
| MaxCre | Number(008,2) | Não | Quantidade máxima de recursos que podem ser alocados p/ fabricação de cada unidade do produto |
| LotTec | Number(010,3) | Sim | Lote Técnico ideal, de fabricação a nível de Operação |
| DtiVal | Date | Sim | Data de Validade inicial p/ utilização desta Operação (Opcional) |
| DtfVal | Date | Sim | Data de Validade final p/ utilização desta Operação (Opcional) |
| SelCus | String(001) | Não | Indica se o item será considerado para a área de custos (importação da ficha técnica) |
| VerRot | String(015) | Sim | Última versão do roteiro na qual é incrementada em cada nova alteração |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou o registro |
| HorGer | Number(005,0) | Sim | Hora da geração da versão |
| QtdCre | Number(008,2) | Sim | Quantidade de recursos (máquinas/pessoas) que serão efetivamente utilizados |
| NecLig | String(001) | Sim | Seq. operacional será ligada ao Produto específico que o utiliza |

---

## Chave Primária

- CodEmp
- CodRot
- CodEtg
- SfxEtr
- SeqRot
- SfxSeq
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
